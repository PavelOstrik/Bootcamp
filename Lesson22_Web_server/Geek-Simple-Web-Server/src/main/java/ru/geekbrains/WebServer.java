package ru.geekbrains;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

public class WebServer {

    public static void main(String[] args) {
        // Создаем класс и объявляем переменную такого типа
        // Присваиваем ей новый экземпляр такого класса
        // В качестве параметра указываем порт, на котором хотим разместить наш ServerSocket
        // Запиись вида try (...) позволяет нам по окончанию выполнения этого блока
        // освободить ресурс, ранее нами зарезервированный
        try (ServerSocket serverSocket = new ServerSocket(8088)) {

            // Чтобы работа сервера не заканчивалась после выполнения кода оборачиваем его в бесконечный цикл
            while(true) {
                Socket socket = serverSocket.accept(); // метод для ожидания подключения к порту
                // на этом методе программа зависает и ждет пока кто то к нам не подключится
                // Как только он подлкючится нам будет возвращен экземпляр класса socket (в переводе розетка)
                // и мы сможем с этим клиентом коммуницировать
                // обратится к нашему серверу в качетсве клмента в бразуре вводим
                // localhost:8088 и нажать enter (это зарезервированное доменное имя для локального подключения)
                System.out.println("New client connected!");

                // Чтобы не считывать данные посимвольно и не гадать где конец строки, а считвать данные построчно
                // Пишем класс BufferedReader
                BufferedReader input = new BufferedReader(
                        // Для преобразования набора байтов в текст пишем класс InputStreamReader
                        new InputStreamReader(
                                // Метод позволяющий получить поток данных отправленных сервером getInputStream()
                                // В качестве второго параметра указываем кодировку StandardCharsets.UTF_8
                                socket.getInputStream(), StandardCharsets.UTF_8));

                // Создаем класс для считывания информации и переменную в которую мы будет записывать её
                PrintWriter output = new PrintWriter(socket.getOutputStream());

                // С помощью данного цикла ждем пока плявится что то , что мы можем считать их потока данных
                // Как что то появляется он возвращает true
                // пока идет false он висит
                while (!input.ready()) ;

                // Пока метод input.ready() истина
                while (input.ready()) {
                    // Считывваем построчно информацию, которая приходит от браузера и сразу выводим её на экран
                    // с помощью метода System.out.println
                    System.out.println(input.readLine());
                }

                // Записываем в переменную output информацию с помощью метода println
                // Если запрос на сервер успешный, то отвесаем на успешный http запрос 200 ok
                // В свою очередб кода, начинающиеся с 4 означают ошибку на стороне клиента
                // если с 5 то ошибка на стороне сервера
                output.println("HTTP/1.1 200 OK");
                // Добавляем заголовок, который будет содержать кодировку
                // мф хотим передать текст в формате html (text/html)
                output.println("Content-Type: text/html; charset=utf-8");
                // Для того чтобы указать что все заголовки закончились и далее начинается содержимое того файла
                // которое было запрошено необходимо добавить пустую строку
                output.println();
                output.println("<h1>Привет от сервера!</h1>");
                // для того чтобы инофрмация гарантированно отправилась вызываем метод flush()
                output.flush();

                // Закрываем потоки по окончанию обработки
                input.close();
                output.close();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}