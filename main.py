# Project preview

# Frontend -> user sees/interacts
# Backend -> Logic behind the website

# pip install flet - for apps and webs

# Title ChatOnline

# Start chat button
    #popup
        # Welcome to the chat
        # Write your name
        # Join chat


# Chat
    # Gabriel joined the chat
    # User messages
# Field to enter message
# Send button

import flet as ft

def main(page):
    text = ft.Text('Online Chat') 


    username = ft.TextField(label='Write your name')

    chat = ft.Column()

    def send_message_tunel(information):
        chat.controls.append(ft.Text(information))
        page.update()
        

    page.pubsub.subscribe(send_message_tunel)


    def send_message(event):
        # Put the user's name in the message
        message_field_text = f'{username.value}: {message_field.value}'        


        page.pubsub.send_all(message_field_text)
        # Clear the message field
        message_field.value = ''

        page.update()

    message_field = ft.TextField(label='Write your message here', on_submit=send_message)

    send_button = ft.ElevatedButton('Enviar', on_click=send_message)


    def enter_chat(event):
        # close the popup
        popup.open = False

        # Remove the start chat button from the screen
        page.remove(start_button)
        # Add CHAT
        page.add(chat)
        #create the send message field
        message_line = ft.Row(
            [message_field, send_button]
        )
        page.add(message_line)
        # send message button

        text = f'{username.value} enter the chat!'
        page.pubsub.send_all(text)
        page.update()


    popup = ft.AlertDialog(

        open = False,
        modal = True,
        title = ft.Text('Welcome to the Online Chat'),
        content =  username,
        actions = [ft.ElevatedButton('Entrar', on_click=enter_chat)]
    )


    def start_chat(event):   # always an on_click event
        page.dialog = popup
        popup.open = True
        page.update()

    start_button = ft.ElevatedButton('Start Chat', on_click= start_chat)



    page.add(text)
    page.add(start_button)


# ft.app(main)

ft.app(main, view=ft.WEB_BROWSER)
