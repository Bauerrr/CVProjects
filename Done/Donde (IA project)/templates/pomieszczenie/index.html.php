<?php

/** @var \App\Model\pomieszczenie[] $pomieszczenia */
/** @var \App\Service\Router $router */
use \App\Model\Pietro;
$title = 'Pomieszczenie List';
$bodyClass = 'index';

ob_start(); 
session_start();
?>
    <div class = "nawigacja">
        <h2>Panel Administratora</h2>
        <ul>
            
            <li><a href="<?= $router->generatePath('pracownik-index');?>">Pracownicy</a></li>

            <li><a href="<?= $router->generatePath('pomieszczenie-index');?>" style="color: #006AFF">Pomieszczenia</a></li>

            <li><a href="<?= $router->generatePath('pracownik_pomieszczenie-index');?>">Pracownicy-Pomieszczenia</a></li>

            <li><a href="<?= $router->generatePath('Pietro-index');?>">Piętra</a></li>
        </ul>
    </div>

    <a id="dodajPom" href="<?= $router->generatePath('pomieszczenie-create') ?>">Dodaj pomieszczenie</a>

    <ul class="index-list">
        <?php foreach ($pomieszczenia as $pomieszczenie): ?>
            <li><p><?= $pomieszczenie->getNumer()." ".Pietro::find($pomieszczenie->getPietro_id())->getNazwa() ?></p>
                <ul class="action-list">
                    <li><a href="<?= $router->generatePath('pomieszczenie-show', ['id' => $pomieszczenie->getPomieszczenie_id()]) ?>">Details</a></li>
                    <li><a href="<?= $router->generatePath('pomieszczenie-edit', ['id' => $pomieszczenie->getPomieszczenie_id()]) ?>">Edit</a></li>
                </ul>
            </li>
        <?php endforeach; ?>
    </ul>

<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
