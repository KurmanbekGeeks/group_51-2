import flet as ft

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    
    greeting_text = ft.Text("Привет, мир!")

    name_input = ft.TextField(label="Введите ваше имя:", autofocus=True)

    def on_button_click(e):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f"Привет, {name}!"
            greet_button.text = 'Поздороваться снова'
            name_input.value = ''
        else:
            greeting_text.value = "Пожалуйста, введите ваше имя!"

        page.update()

    greet_button = ft.ElevatedButton("Поздороваться", on_click=on_button_click)

    page.add(greeting_text, name_input, greet_button)

ft.app(target=main)

# ft.app(target=main, view=ft.WEB_BROWSER)


