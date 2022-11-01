namespace Client  // Пространство имен, чтобы одни и те же переменные
// использовать в разных файлах. В одном namespace может лежать несколько классов
// Здесь мы работаем с классами
{
    class Program
    {
        // Создаем функцию для запуска нашей программы
        static void Main(string[] args)
        {
            Console.WriteLine("Это наш клиент");
            // namespace использовали пространство имен чтобы использовать
            // переменную ourClient из файла OurClient
            // new OurClient() создаем нового клиента
            OurClient ourClient = new OurClient();
        }
    }
}
