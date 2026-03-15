from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class AfghanServicesFinder(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        title = Label(text='Afghan Services Finder',
                      size_hint_y=0.1, bold=True, font_size='20sp')
        main_layout.add_widget(title)

        grid = GridLayout(cols=2, spacing=10, size_hint_y=0.9)

        services = [
            ('Doctors', 'find_doctors'),
            ('Mechanics', 'find_mechanics'),
            ('Electricians', 'find_electricians'),
            ('Restaurants', 'find_restaurants'),
            ('Hotels', 'find_hotels'),
        ]

        for service_name, callback in services:
            btn = Button(text=service_name, size_hint_y=None, height=100)
            btn.bind(on_press=lambda x, s=service_name: self.show_service(s))
            grid.add_widget(btn)

        main_layout.add_widget(grid)
        return main_layout

    def show_service(self, service):
        content = BoxLayout(orientation='vertical')
        content.add_widget(
            Label(text=f'Nearby {service}:\n\nFeature coming soon!'))

        popup = Popup(title=service, content=content, size_hint=(0.9, 0.6))
        popup.open()


if __name__ == '__main__':
    AfghanServicesFinder().run()
