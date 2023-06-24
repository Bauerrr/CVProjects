<?php

/** @var \App\Model\Pietro[] $Pietra */
/** @var \App\Service\Router $router */

$title = 'Pietro List';
$bodyClass = 'index';

ob_start(); 
session_start();
?>
    <div class = "nawigacja">
        <h2>Panel Administratora</h2>
        <ul>
            
            <li><a href="<?= $router->generatePath('pracownik-index');?>">Pracownicy</a></li>

            <li><a href="<?= $router->generatePath('pomieszczenie-index');?>">Pomieszczenia</a></li>

            <li><a href="<?= $router->generatePath('pracownik_pomieszczenie-index');?>">Pracownicy-Pomieszczenia</a></li>

            <li><a href="<?= $router->generatePath('Pietro-index');?>" style="color: #006AFF">Piętra</a></li>
        </ul>
    </div>

    <a id="dodajPietro" href="<?= $router->generatePath('Pietro-create') ?>">Dodaj piętro</a>

    <ul class="index-list">
        <?php foreach ($Pietra as $Pietro): ?>
            <li><p><?= $Pietro->getNazwa() ?></p>
                <ul class="action-list">
                    <li><a href="<?= $router->generatePath('Pietro-show', ['id' => $Pietro->getPietroId()]) ?>">Details</a></li>
                    <li><a href="<?= $router->generatePath('Pietro-edit', ['id' => $Pietro->getPietroId()]) ?>">Edit</a></li>
                </ul>
            </li>
        <?php endforeach; ?>
    </ul>

<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
