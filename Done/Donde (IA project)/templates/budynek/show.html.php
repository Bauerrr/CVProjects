<?php

/** @var \App\Model\budynek $post */
/** @var \App\Service\Router $router */

$title = "{$post->getNazwa()} ({$post->getBudynekId()})";
$bodyClass = 'show';

ob_start(); ?>
    <h1><?= $post->getNazwa() ?></h1>
    <article>
        <?= $post->getKraj();?>
        <?= $post->getMiasto();?>
        <?= $post->getKodPocztowy();?>
        <?= $post->getUlica();?>
        <?= $post->getNrBudynku();?>
    </article>

    <ul class="action-list">
        <li> <a href="<?= $router->generatePath('budynek-index') ?>">Back to list</a></li>
        <li><a href="<?= $router->generatePath('budynek-edit', ['id'=> $post->getBudynekId()]) ?>">Edit</a></li>
    </ul>
<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
