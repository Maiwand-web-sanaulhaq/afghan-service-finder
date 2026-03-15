from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window

Window.size = (360, 640)

class AfghanServicesFinder(App):
    icon = 'icon.png'
    title = 'Afghan Services Finder'

    def build(self):
        main_layout = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=8
        )

        title = Label(
            text='Afghan Services Finder',
            size_hint_y=None,
            height=50,
            bold=True,
            font_size='18sp',
            color=(1, 1, 1, 1)
        )
        main_layout.add_widget(title)

        grid = GridLayout(
            cols=2,
            spacing=10,
            size_hint_y=None,
            padding=5
        )
        grid.bind(minimum_height=grid.setter('height'))

        services = [
            ('Doctors', 'Doctors'),
            ('Mechanics', 'Mechanics'),
            ('Electricians', 'Electricians'),
            ('Restaurants', 'Restaurants'),
            ('Hotels', 'Hotels'),
            ('Pharmacies', 'Pharmacies'),
            ('Schools', 'Schools'),
            ('Taxis', 'Taxis'),
        ]

        for service_name, key in services:
            btn = Button(
                text=service_name,
                size_hint_y=None,
                height=90,
                font_size='14sp',
                background_color=(0.1, 0.5, 0.8, 1)
            )
            btn.bind(on_press=lambda x, s=service_name: self.show_service(s))
            grid.add_widget(btn)

        main_layout.add_widget(grid)
        return main_layout

    def show_service(self, service):
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(
            Label(text=f'Nearby {service}:\n\nFeature coming soon!'))
        close_btn = Button(
            text='Close',
            size_hint_y=None,
            height=40,
            background_color=(0.9, 0.2, 0.2, 1)
        )
        popup = Popup(
            title=service,
            content=content,
            size_hint=(0.9, 0.6)
        )
        close_btn.bind(on_press=popup.dismiss)
        content.add_widget(close_btn)
        popup.open()

if __name__ == '__main__':
    AfghanServicesFinder().run()
