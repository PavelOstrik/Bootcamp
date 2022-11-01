// Подключаем библиотеки для работы с TCP 
using System.Net.Sockets;
using System.Net;
using System.Text;

namespace Server
{
    class OurServer
    {
        // Чтобы принимать подключения от клиентов нам нужно следующее поле: TcpListener
        TcpListener server;

        // Как только создаётся сервер мы указываем TcpListener ipAdress и порт
        public OurServer()
        {
            server = new TcpListener(IPAddress.Parse("127.0.0.1"), 5555);
            server.Start();
            // Так же держим текущее подключение
            LoopClients();  
        }

        void LoopClients()
        {
            while (true)  // создаем бесконечный цикл
            {   
                // Как только клиент подключается к нашему серверу создается client
                // который мы будем обрабатывать на сервере
                TcpClient client = server.AcceptTcpClient();
                // Будем делать обработку наших клиентов с помощью потоков Thread
                // Кладем каждого клиента в отдельный поток
                Thread thread = new Thread(() => HandleClient(client));
                // Запускаем наш поток
                thread.Start();
            }
        }

        // Сделаем отдельную функцию, которая будет дерджать соединение с клиентом
        void HandleClient(TcpClient client)
        {
            // Создаем поток, который будет считывать сообщения от клиента
            StreamReader sReader = new StreamReader(client.GetStream(), Encoding.UTF8);
            // Создаем поток, который будет отправлять данные нашему клиенту
            StreamWriter sWriter = new StreamWriter(client.GetStream(), Encoding.UTF8);

            while (true)
            {   
                // Получаем нашу сроку из потока
                string message = sReader.ReadLine();
                // И выводим её на экран нашего сервера
                Console.WriteLine($"Клиент написал - {message}");

                Console.WriteLine("Дайте сообщение клиенту: ");
                string answer = Console.ReadLine();
                sWriter.WriteLine(answer);
                sWriter.Flush();
            }
        }
    }
}