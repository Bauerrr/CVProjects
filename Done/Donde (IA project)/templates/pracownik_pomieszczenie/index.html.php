<?php

/** @var \App\Model\pracownik_pomieszczenie[] $pracownicy_pomieszczenia */
/** @var \App\Service\Router $router */

$title = 'Pomieszczenie List';
$bodyClass = 'index';

ob_start(); 
session_start();
?>
    
    <div class = "nawigacja">
        <h2>Panel Administratora</h2>
        <ul>
            
            <li><a href="<?= $router->generatePath('pracownik-index');?>">Pracownicy</a></li>

            <li><a href="<?= $router->generatePath('pomieszczenie-index');?>">Pomieszczenia</a></li>

            <li><a href="<?= $router->generatePath('pracownik_pomieszczenie-index');?>" style="color: #006AFF">Pracownicy-Pomieszczenia</a></li>

            <li><a href="<?= $router->generatePath('Pietro-index');?>">Piętra</a></li>
        </ul>
    </div>

    <a id="dodajPracPom" href="<?= $router->generatePath('pracownik_pomieszczenie-create') ?>">Create new</a>

    <ul class="index-list">
        <?php foreach ($pracownicy_pomieszczenia as $pracownik_pomieszczenie): ?>
            <li><p><?= $pracownik_pomieszczenie->getPracownik_pomieszczenie_id() ?></p>
                <ul class="action-list">
                    <li><a href="<?= $router->generatePath('pracownik_pomieszczenie-show', ['id' => $pracownik_pomieszczenie->getPracownik_pomieszczenie_id()]) ?>">Details</a></li>
                    <li><a href="<?= $router->generatePath('pracownik_pomieszczenie-edit', ['id' => $pracownik_pomieszczenie->getPracownik_pomieszczenie_id()]) ?>">Edit</a></li>
                </ul>
            </li>
        <?php endforeach; ?>
    </ul>

<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';