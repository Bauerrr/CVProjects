<?php

/** @var \App\Model\pomieszczenie $pomieszczenie */
/** @var \App\Model\Pietro $pietro */
/** @var \App\Service\Router $router */
use \App\Model\Pietro;

$title = "{$pomieszczenie->getNumer()} ({$pomieszczenie->getPomieszczenie_id()})";
$bodyClass = 'show';

ob_start(); 
session_start();
?>
    <h1><?= $pomieszczenie->getNumer()." ".Pietro::find($pomieszczenie->getPietro_id())->getNazwa() ?></h1>
    <article>
        <?= Pietro::find($pomieszczenie->getPietro_id())->getNazwa()?>
    </article>

    <ul class="action-list">
        <li> <a href="<?= $router->generatePath('pomieszczenie-index') ?>">Back to list</a></li>
        <li><a href="<?= $router->generatePath('pomieszczenie-edit', ['id'=> $pomieszczenie->getPomieszczenie_id()]) ?>">Edit</a></li>
    </ul>
<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
