"""
主窗口GUI
"""

import asyncio
import flet as ft

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet1111")))

ft.app(main)