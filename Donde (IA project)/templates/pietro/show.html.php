<?php

/** @var \App\Model\Pietro $Pietro */
/** @var \App\Service\Router $router */
use \App\Model\budynek;
$title = "{$Pietro->getBudynekId()} ({$Pietro->getPietroId()})";
$bodyClass = 'show';

ob_start(); 
?>
    <h1><?= $Pietro->getNazwa() ?></h1>
    <article>
        <?= budynek::find($Pietro->getBudynekId())->getNazwa()." ".$Pietro->getNazwa();?>
    </article>

    <ul class="action-list">
        <li> <a href="<?= $router->generatePath('Pietro-index') ?>">Back to list</a></li>
        <li><a href="<?= $router->generatePath('Pietro-edit', ['id'=> $Pietro->getPietroId()]) ?>">Edit</a></li>
    </ul>
<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
