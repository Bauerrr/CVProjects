<?php

/** @var \App\Model\pracownik_pomieszczenie $pracownik_pomieszczenie */
/** @var \App\Service\Router $router */

$title = "Poka";
$bodyClass = 'show';

ob_start(); 
session_start();
?>
    <h1><?= $pracownik_pomieszczenie->getPracownik_id(); ?></h1>
    <article>
        <?= $pracownik_pomieszczenie->getPracownik_pomieszczenie_id();?>
    </article>

    <ul class="action-list">
        <li> <a href="<?= $router->generatePath('pracownik_pomieszczenie-index') ?>">Back to list</a></li>
        <li><a href="<?= $router->generatePath('pracownik_pomieszczenie-edit', ['id'=> $pracownik_pomieszczenie->getPracownik_pomieszczenie_id()]) ?>">Edit</a></li>
    </ul>
<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
