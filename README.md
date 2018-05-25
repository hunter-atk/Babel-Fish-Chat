#Babel Fish Chat
##5-Hour Hackathon Challenge

For this challenge, we were given 5 hours to develop a project using websockets. We had 15 minutes to decide what we would build, and we decided to aim to build a chat application which enables people from around the world to communicate with and understand each other regardless of their chosen language. This idea was inspired by the babel fish in Douglas Adams' Hitchhiker's Guide to the Galaxy. 

List of features:
- A chat window consisting of a canvas with an under-the-sea-esque background.
- A fish avatar for each chat participant, which can "swim" around the ocean-like canvas with keyboard arrow controls.
- Two input fields beneath the window. One for the user to enter their handle, one to enter a message.
- A submit button which will render the user's message in a chat bubble above their fish avatar in the chat window for 10 seconds, or until it is replaced with another message.
- A drop-down select field above the chat window with multiple languages the user can select from. All incoming messages from other chat participants will be translated into the selected language.

Technologies used:
- JavaScript
- socket.io
- Google Translate API

What we accomplished:
- I created the server, set up the websocket functionalities, and created the chatbox on the front end. After two hours, we had a working chat app which used websockets to connect multiple clients to the server and update the contents of the chat window in real time. 
- Tim Barnes created a canvas with a fun backdrop and a moving avatar. Mid-way through the hackathon, we pivoted from an ocean-themed canvas/avatar to an "International Hotel" with a people-like avatar which could move around the canvas. We didn't get as far as rendering multiple avatars to the window and having a chat bubble appear above them when a message was sent. In the end we had a separate chat box and interactive canvas. 
- Nathan Keolasy researched the API for Google Translate. In the end we simply incoorported a Google Translate plugin due to challenges with implementing the API on the front-end.

Challenges:
- Our biggest challenge was figuring out how to implement Google's translate API. It only works when you run their code on your server, or so it seemed at the time. Originally, we wanted the app to take a message from a client, send it to the server through the websocket connection, where it would then be sent to all clients through all websocket connections, and translated on the front-end for each client differently depending on their language of choice. If we were to translate the message in the back-end, we would need to somehow access the language input for each individual client on the back end, translate the message x number of times, and send specific strings back to specific clients. Doable, I'm sure, but at this point we had just a couple hours left. We reapproached the problem and solved it by simply copy-pasting a Google Translate plugin into our HTML document, which functions nearly the same way as our intended "Pick a Language" dropdown selector would. This way, however, all text on the page, regardless of its original language, is translated to the user's language of choice.
- Creating the interactive canvas was also a challenge. Tim was able to create a canvas with a gif background, and was able to move a little person around the canvas with his arrow controls. Learning to create this took quite a bit more time than we expected, but given more time, we believe we could've managed to render multiple moving figures on the page. Preferably fish!


