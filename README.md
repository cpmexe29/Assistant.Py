__Assistant.Py__

<H1> Ассистент с голосовым управлением </H1>

<p> Используемые библиотеки: </p>
<ul>  
    <li> speech_recognition </li>
    <li> pyttsx3 </li>
    <li> os </li>
    <li> webbrowser </li>
</ul>

<p> Используемые классы: </p>
<ul>  
    <li> VoiceAssistant </li>
</ul>

<p> Используемые функции: </p>
<ul>  
    <li> setup_assistant_voice </li>
    <li> play_voice_assistant_speech </li>
    <li> record_and_recognize_audio </li>
</ul>
<p> Функции команд: </p>
<ul>  
    <li> search_google </li>
    <li> goodbye </li>
    <li> shutdown_pc </li>
    <li> restart_pc </li>
    <li> search_youtube </li>
</ul>

<H2> Точка старта </H2>
  <ol>  
      <li> Инициализация инструментов распознавания и ввода речи </li>
      <li> Инициализация инструмента синтеза речи </li>
      <li> Настройка данных голосового помощника </li>
      <li> Установка голоса по умолчанию </li>
      <li> Условно бесконечный цикл <i> while </i> (ассистент в работе) </li>
        <ul>  
            <li> <b> __Cтарт записи речи </b>__ </li>
            <li> Проверка на наличие текста </li>
            <li> Удаление временного файла текста (отладка) </li>
            <li> Обработка команды </li>
            <li> Выполнение функций по заданным командам</li>
          </ul>
  </ol>

