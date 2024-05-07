"""
主窗口GUI
"""

import asyncio
import flet as ft

import configparser
import requests
import json


def main(page: ft.Page):
    # 载入设置
    cfg = configparser.ConfigParser()
    cfg.read("main.cfg", encoding="utf-8")

    # 全局变量
    global g_task_list
    url_dataset = ""
    url_remote_gpt = "http://127.0.0.1:5102"
    url_local_gpt = "http://127.0.0.1:5102"
    url_manim = "http://127.0.0.1:5103"
    g_ping_gpt = 0
    g_ping_dataset = 0
    g_version_gpt = "v"
    g_version_dataset = "v"
    g_task_path = "./data"
    g_task_list = []

    # 读取Readme作为文档
    with open("./README.md", encoding="utf-8") as doc_mk:
        doc_mk = doc_mk.read()

    def bottom_items(label: str):
        ct = ft.Container(
            content=ft.Chip(ft.Text(label), on_click=None),
            alignment=ft.alignment.center,
            width=150,
            height=50,
            # bgcolor=ft.colors.AMBER,
            border_radius=ft.border_radius.all(5),
        )
        return ct

    def create_bottom_items():
        items = [
            bottom_items(f"数据仓库|{g_ping_dataset}ms|{g_version_dataset}"),
            bottom_items(f"remote-GPT|{g_ping_gpt}ms|{g_version_gpt}"),
            bottom_items(f"local-GPT|{g_ping_dataset}ms|{g_version_dataset}"),
        ]
        return items

    def pick_files_result(e: ft.FilePickerResultEvent):
        global g_task_list
        print(e.path, e.name, e.data, e.files)
        text_task_file_path.value = str(json.loads(e.data)["files"][0]["path"])
        with open(
            str(json.loads(e.data)["files"][0]["path"]), encoding="utf-8"
        ) as file:
            g_task_list = file.readlines()
            g_task_list = [i.replace("\n", "") for i in g_task_list]

        page.update()

    def do_task(e: ft.TapEvent):
        for index, task in enumerate(g_task_list):
            Progress_part.value = (index + 1) / len(g_task_list)
            Progress_part.update()
            textfield_step1.value = task
            textfield_step1.update()
            print(task)
            re = requests.post(f'{url_remote_gpt}/task_sim',json={'descip':task})
            gpt_res = str(re.json())
            
            textfield_step2.value = gpt_res
            textfield_step2.update()

            re = requests.post(f'{url_manim}/task',json={'task':gpt_res})
            manim_res = str(re.json())

    text_task_file_path = ft.Text()  # 任务文件路径
    textfield_step1 = ft.TextField(
        label="Step1--GPT任务",
        multiline=True,
        min_lines=1,
        max_lines=3,
    )
    textfield_step2 = ft.TextField(
        label="Step2--GPT规划",
        multiline=True,
        min_lines=1,
        max_lines=3,
        width=500
    )

    Tab_main = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        enable_feedback=False,
        mouse_cursor=ft.MouseCursor("click"),
        scrollable=True,
        tabs=[
            ft.Tab(
                text="浏览",
                icon=ft.icons.SEARCH,
                content=ft.Container(
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("First name")),
                            ft.DataColumn(ft.Text("Last name")),
                            ft.DataColumn(ft.Text("Age"), numeric=True),
                        ],
                    )
                ),
            ),
            ft.Tab(
                text="GPT",
                icon=ft.icons.DESKTOP_WINDOWS_ROUNDED,
                content=ft.Column(
                    alignment=ft.alignment.center,
                    expand=True,
                    controls=[
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "选择任务文件",
                                    on_click=lambda _: pick_files_dialog.pick_files(
                                        allow_multiple=False
                                    ),
                                ),
                                text_task_file_path,
                            ]
                        ),
                        ft.Row([textfield_step1, textfield_step2]),
                        ft.Row(
                            [
                                ft.Image("defalt.jpg", width=200, height=200),
                                ft.TextField(
                                    label="Step4--RGPT描述",
                                    multiline=True,
                                    min_lines=1,
                                    max_lines=3,
                                ),
                            ]
                        ),
                        ft.ElevatedButton("开始任务", on_click=do_task),
                    ],
                ),
            ),
            ft.Tab(
                text="统计", icon=ft.icons.ALIGN_VERTICAL_BOTTOM, content=ft.Text("123")
            ),
            ft.Tab(
                text="设置",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
            ft.Tab(
                text="文档",
                icon=ft.icons.READ_MORE,
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
    Progress_main = ft.ProgressBar(value=0)
    Progress_part = ft.ProgressBar(value=0)
    Tab_but = ft.Row(controls=create_bottom_items())
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)
    page.title = "数据管理中心  Dataset Manager  V" + cfg["main"]["version"]
    page.add(Tab_main)
    page.add(Progress_main)
    page.add(Progress_part)
    page.add(Tab_but)
    page.fonts = {"SiYuan": "fonts/SourceHanSansSC-Regular-2.otf"}
    page.theme = ft.Theme(font_family="SiYuan")

    page.update()


ft.app(main)
