<?php

/** @var \App\Model\pracownik $post */
/** @var \App\Service\Router $router */

$title = "{$post->getTytul()} {$post->getImie()} {$post->getNazwisko()}";
$bodyClass = 'show';

ob_start(); 
session_start();
?>
    <h1><?= $post->getNazwisko() ?></h1>
    <article>
        <?= $post->getImie();?>
        <?= $post->getTytul();?>
        <?= $post->getGabinet();?>
    </article>

    <ul class="action-list">
        <li> <a href="<?= $router->generatePath('pracownik-index') ?>">Back to list</a></li>
        <li><a href="<?= $router->generatePath('pracownik-edit', ['id'=> $post->getPracownikId()]) ?>">Edit</a></li>
    </ul>
<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
