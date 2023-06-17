<?php

/** @var \App\Service\Router $router */
$templating = new \App\Service\Templating();
$title = 'Main strona';
$bodyClass = 'index';



ob_start();
session_start();


if(!isset($_SESSION['login']) || $_SESSION['login'] == ''){
    $path = $router->generatePath('');
    $router->redirect($path);
    
}
?>

<html>
    <div class = "nawigacja">
    <h2>Panel Administratora</h2>
        <ul>
            
            <li><a href="<?= $router->generatePath('pracownik-index');?>">Pracownicy</a></li>

            <li><a href="<?= $router->generatePath('pomieszczenie-index');?>">Pomieszczenia</a></li>

            <li><a href="<?= $router->generatePath('pracownik_pomieszczenie-index');?>">Pracownicy-Pomieszczenia</a></li>

            <li><a href="<?= $router->generatePath('Pietro-index');?>">Piętra</a></li>
        </ul>
    </div>
</html>

<?php

$main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';