//сортировка подсчетом

int[] array = {-10, -5, -9, 0, 2, 5, 1, 3, 1, 0, 1};
int[] sortedArray = CountingSortExtended(array);

//CountingSort(array);

Console.WriteLine(string.Join(", ", sortedArray));

// Функция для массива, состоящего только из цифр от 0 до 9
/*
void CountingSort(int[] inputArray)
{
    int[] counters = new int[10]; //массив повторений

    for (int i = 0; i < inputArray.Length; i++)
    {
        counters[inputArray[i]]++;
        // ourNumber = inputArray[i];
        // counters[ourNumber]++;
    }

    int index = 0;
    for (int i = 0; i < counters.Length; i++)
    {
        for (int j = 0; j < counters[i]; j++)
        {
            inputArray[index] = i;
            index++;
        }
    }
}
*/

// Расширенный метод, сортирующий числа больше 9 и отрицательные числа
int[] CountingSortExtended(int[] inputArray)
{
    int max = inputArray.Max();
    int min = inputArray.Min();

    int offset = -min; // Сдвиг, чтобы все элементы поместились в новый массив
    int[] sortedArray = new int[inputArray.Length];
    int[] counters = new int[max + offset + 1];



    for (int i = 0; i < inputArray.Length; i++)
    {
        counters[inputArray[i] + offset]++;
    }

    int index = 0;
    for (int i = 0; i < counters.Length; i++)
    {
        for (int j = 0; j < counters[i]; j++)
        {
            sortedArray[index] = i - offset;
            index++;
        }
    }

    return sortedArray;
}
