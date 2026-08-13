#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
一键启动器 (start.py)
=====================
自动启动本地静态服务器并提供 Demo 页面访问。

用法:
    python start.py            # 默认端口 8090，自动打开浏览器
    python start.py --port 9000
    python start.py --no-browser

说明:
    - 优先使用 8090，若被占用自动 +1 试探（最多 10 次）。
    - 用默认浏览器打开 http://localhost:<port>。
    - 按 Ctrl+C 停止服务器。
    - 放在项目根目录，与 demo/ 同级即可。
"""

import argparse
import os
import socket
import subprocess
import sys
import time
import webbrowser

ROOT = os.path.dirname(os.path.abspath(__file__))
DEMO_DIR = os.path.join(ROOT, "demo")


def find_free_port(start: int, max_tries: int = 10) -> int:
    """从 start 端口开始找一个可用端口"""
    for offset in range(max_tries):
        port = start + offset
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    return -1


def is_port_listening(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) == 0


def main():
    parser = argparse.ArgumentParser(description="防汛预警系统 Demo 一键启动")
    parser.add_argument("--port", type=int, default=8090, help="起始端口 (默认 8090)")
    parser.add_argument("--no-browser", action="store_true", help="不自动打开浏览器")
    parser.add_argument("--host", default="127.0.0.1", help="监听地址 (默认 127.0.0.1)")
    args = parser.parse_args()

    if not os.path.isdir(DEMO_DIR):
        print(f"[错误] 未找到 demo 目录: {DEMO_DIR}")
        print("请确认 start.py 与 demo/ 处于同一项目根目录。")
        sys.exit(1)

    port = find_free_port(args.port)
    if port == -1:
        print(f"[错误] 从 {args.port} 起连续 {10} 个端口均被占用，请手动指定 --port。")
        sys.exit(1)

    url = f"http://{args.host}:{port}/"

    # 启动静态服务器（后台子进程，绑定 demo 目录）
    proc = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port),
         "--bind", args.host, "--directory", DEMO_DIR],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # 等待服务器就绪
    ready = False
    for _ in range(30):
        if is_port_listening(port):
            ready = True
            break
        time.sleep(0.2)

    if not ready:
        print("[警告] 服务器启动较慢，请稍后手动访问。")
    else:
        print("=" * 60)
        print("  河南省中东部防汛与台风极端降雨监控预警系统")
        print("  ZHX NEXUS Studio · Demo 一键启动")
        print("=" * 60)
        print(f"  ✅ 本地服务器已启动")
        print(f"  🌐 访问地址: {url}")
        print(f"  ⏹  停止: 在终端按 Ctrl+C")
        print("=" * 60)

    if not args.no_browser:
        try:
            webbrowser.open(url)
        except Exception:
            print(f"[提示] 无法自动打开浏览器，请手动访问: {url}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[信息] 正在停止服务器...")
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
        print("[信息] 已停止。再见。")


if __name__ == "__main__":
    main()
