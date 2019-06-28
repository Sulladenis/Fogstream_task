# Fogstream_task
task execution

Скриптом заливаеются данные с суперпользователем
username: admin
email: admin@localhost
password: message

Демонстрационный пользователь - если зайти под ним видно несколько последних сообщений
username: nata
email: nata@localhost
password: message2000

Письмо отправляется в консоль с данными о пользователе из http://jsonplaceholder.typicode.com/users

git clone https://github.com/Sulladenis/Fogstream_task.git
cd Fogstream_task/
sudo docker build -t django .
sudo docker run -it -p 8000:8000 --rm --name my-app django
http://localhost:8000/main

