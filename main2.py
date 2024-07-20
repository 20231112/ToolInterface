import flet as ft

def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else ""
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.title = "Tool interface" 
    page.overlay.append(pick_files_dialog)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    
    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Select your input files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ],alignment=ft.MainAxisAlignment.CENTER,
        )
    )
ft.app(target=main, view=ft.AppView.WEB_BROWSER)