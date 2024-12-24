import requests
import json
import socket

# 配置部分
CLOUDFLARE_API_URL = "https://api.cloudflare.com/client/v4"
CLOUDFLARE_API_TOKEN = "<your_cloudflare_api_token>"  # 替换为你的 Cloudflare API Token
ZONE_ID = "<your_zone_id>"  # 替换为你的 Zone ID
RECORD_ID = "<your_record_id>"  # 替换为你的 DNS 记录 ID
RECORD_NAME = "example.com"  # 替换为你的域名
RECORD_TYPE = "A"  # 记录类型 (一般是 A 或 AAAA)

# 获取当前公网 IPv4 地址
def get_public_ip():
    try:
        response = requests.get("http://ifconfig.me/ip")
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        print(f"获取公网 IP 失败: {e}")
        return None

# 更新 DNS 记录
def update_dns_record(ip):
    url = f"{CLOUDFLARE_API_URL}/zones/{ZONE_ID}/dns_records/{RECORD_ID}"
    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
        "Content-Type": "application/json",
    }
    data = {
        "type": RECORD_TYPE,
        "name": RECORD_NAME,
        "content": ip,
        "ttl": 1,  # 自动 TTL
        "proxied": False,  # 如果需要通过 Cloudflare 代理，可以设置为 True
    }

    try:
        response = requests.put(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        if result.get("success"):
            print(f"DNS 记录更新成功: {ip}")
        else:
            print(f"DNS 记录更新失败: {result}")
    except requests.RequestException as e:
        print(f"更新 DNS 记录时出错: {e}")

# 主程序
def main():
    current_ip = get_public_ip()
    if current_ip:
        print(f"当前公网 IP: {current_ip}")
        update_dns_record(current_ip)
    else:
        print("无法获取公网 IP，终止更新 DNS 记录。")

if __name__ == "__main__":
    main()
