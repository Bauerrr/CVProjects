<?php

/** @var \App\Service\Router $router */
$templating = new \App\Service\Templating();
$title = 'Main strona';
$bodyClass = 'index';



ob_start();
?>
<html lang="en">
  <head>
    <style>

      #log1{
        font-size: 20px;
        margin: auto auto;
        text-align: center;
        padding: 375px;
      }

      #close{
        border: none;
        background: none;
        color: #E4E4E4;
        font-size: 40px;
        position: absolute;
      }
      
      #sub{
        background: #27b6f4;
        color: white;
        width: 70px;
        height: 30px;
        font-size: 10px;
        border: none;
        border-radius: 3px;
        margin-left: 160px;
        margin-top: 10px;
      }
    
    </style>
  </head>

  <body>

    <div class="button">
      <button id="close" type='button'>&#10006</button>
    </div>

    <div class="formularz">
      <form id="log1" action="<?= $router->generatePath('login-kurwa') ?>" method="post">
        Login: <input class="lol" type="text" name="login" placeholder="Twoj login"><br>
        Haslo: <input class="lol" type="password" name="haslo" placeholder="Twoje haslo"><br>
        <input id="sub" type="submit" value="Zaloguj sie">
      </form>
    </div>
    
  </body>
</html>

<?php
$main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';