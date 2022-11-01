// Подключаем библиотеки для работы с TCP
using System.Net.Sockets;
using System.Text;

namespace Client
{
    class OurClient
    {
        // TcpClient позволяет работать с TCP
        // client переменная через которую мы это будем делать
        private TcpClient client; 
        // StreamWriter позволяет передавать данные на сервер
        private StreamWriter sWriter;
        // StreamReader позволяет получать данные с сервера
        private StreamReader sReader;

        // Как только будет создаваться наш клиент мы будем передавать ему следующие данные:
        public OurClient()
        {
            // Присваиваем ipAdress нашему клиенту
            // "127.0.0.1" ipAdress позволяющий работать и клиенту и серверу
            // находиться на одном компьютере, отправить запрос самому себе
            // 5555 это номер порта в который должны прийти данные
            // У одного ipAdress может быть несколько портов
            client = new TcpClient("127.0.0.1", 5555); 
            // Устанавливаем поток для получения данных
            sWriter = new StreamWriter(client.GetStream(), Encoding.UTF8);
            // Устанавливаем поток для передачи данных
            sReader = new StreamReader(client.GetStream(), Encoding.UTF8);
            // Как только мы создали клиент и установили соединение с сервером
            // мы должны это соединение удерживать
            HandleCommunication();
        }
        // Чтобы подключение TCP было постоянным пишем следующий метод:
        void HandleCommunication()
        {
            while (true) // бесконечный цикл
            {
                // пишем '>' чтобы понимать что наш сервер работает
                // а справо от '>' уже будет наше сообщение
                Console.Write("> "); 
                // здесь мы будет передавать сообщение от пользователя клиенту
                // В нашем случае пользователь и клиент это одно и тоже
                string message = Console.ReadLine();
                // Отправляем сообщение серверу по установленномцу потоку
                // Здесь сообшение подготовлено для отправки, но еше не отправлено
                sWriter.WriteLine(message);
                // Эта команда говорит о том, что сообшение надо отправить немедленно
                sWriter.Flush();

                string answerServer = sReader.ReadLine();
                Console.WriteLine($"Сервер ответил -> {answerServer}");
            }
        }


    }
}