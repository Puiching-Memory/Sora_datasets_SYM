"""
主窗口GUI
"""

import asyncio
import flet as ft

import configparser

# 载入设置
cfg = configparser.ConfigParser()
cfg.read("main.cfg", encoding="utf-8")

#链接到GPT服务器的延迟
ping = 123

#读取Readme作为文档
with open('./README.md',encoding='utf-8') as doc_mk:
    doc_mk=doc_mk.read()

def main(page: ft.Page):
    page.title = "数据管理中心  Dataset Manager  V" + cfg["main"]["version"]
    Tab_main = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="浏览",
                icon=ft.icons.SEARCH,
                content=ft.Container(
                    ft.DataTable(columns=[ft.DataColumn(ft.Text("First name")),ft.DataColumn(ft.Text("Last name")),ft.DataColumn(ft.Text("Age"), numeric=True),],)
                ),
            ),
            ft.Tab(
                text="GPT",
                icon=ft.icons.SCREEN_SEARCH_DESKTOP,
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="设置",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
            ft.Tab(
                text="文档",
                icon=ft.icons.DOCUMENT_SCANNER_OUTLINED,
                content=ft.Markdown(
                    doc_mk,
                    selectable=True,
                    extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                    on_tap_link=lambda e: page.launch_url(e.data),
                ),
            ),
        ],
        expand=1,
    )

    page.add(Tab_main)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label=f"GPT ping:{ping}ms"),
        ]
    )

    page.update()


ft.app(main)
