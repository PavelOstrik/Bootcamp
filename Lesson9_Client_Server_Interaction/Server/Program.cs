namespace Server
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Это наш сервер");
            // Здесь мы создаём наш сервер и запускаем его
            OurServer server = new OurServer();
        }
    }
}
