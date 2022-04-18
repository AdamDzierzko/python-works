# Works To Do

## Jak uruchomić

w katalogu python-works\works\ wpisac python manage.py runserver\
w przegladarce http://127.0.0.1:8000/\
Logowanie do panelu administratora:\
username: a@a.pl     \
password: a

## Funkcje w programie

##### index
Wyświetla wszystkie zapisane w bazie zadania, wg kolejności ID. Funkcja jest uruchamiana po wejściu na stronę główną \ lub naciśnięcie przycisku 'Strona główna'.

#### add_new_task
Pobiera treść zadania z formularza, następnie dane są przekazywne do funkcji za pomocą funkcji w addtask() w index.js. \ Umożliwia to tworzenie Single Page Application, która posiadania tylko jednen plik html. Widok jest zmieniany dynamicznie \ podczas interakcji z użytkownikiem. Umożliwi to min. szybsze działanie, bez potrzeby ciągłego przeładowywania strony.

#### delete_task
Usuwa wskazane zadanie poprzez naciśnięcie przycisku w etykiecie zadania. Zadanie jest wskazywane poprzez nr ID umieszczony \ w adresie url przy wywoływaniu funkcji.

#### find
Pobiera wpisaną w formularz frazę i przekazuje bezpośrednio do funkcji metodą post. Następnie jest sprawdzana obecność \ szukanej frazy kolejno we wszystkich opisach zadań w bazie danych. Jeżli fraza znajduje się w opisie, pojedyncze zadanie \ jest dodawane do listy. Jeżeli nie to jest pomijany. Lista obiektów jest przekazana do wyświetlenia w pliku index.html. \

#### panel administratora
Dodana wyszukiwarka i wyświetlanie ID zadania opisem na liście.

## Co warto dodać do programu*
- paginator - ograniczy ilość etykiet na stronie
- status etykiety - kryterium wykonalności, kolory, przesuwanie w poziomie
- pozycjonowanie etykiet na liście - można je przesuwać w pionie
- daty
- statystyki
- rozbudowane filtry w wszukiwarce
- zamiana TextField w modelu na RichTextField, co doda konfigurowalny edytor textu
- rozbudowa panelu administratora
