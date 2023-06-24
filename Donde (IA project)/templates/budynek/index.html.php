<?php

/** @var \App\Model\budynek[] $posts */
/** @var \App\Service\Router $router */

$title = 'budynek List';
$bodyClass = 'index';

ob_start(); ?>
    <h1>Posts List</h1>
    <a href="<?= $router->generatePath('budynek-create') ?>">Create new</a>

    <ul class="index-list">
        <?php foreach ($posts as $post): ?>
            <li><h3><?= $post->getNazwa() ?></h3>
                <ul class="action-list">
                    <li><a href="<?= $router->generatePath('budynek-show', ['id' => $post->getBudynekId()]) ?>">Details</a></li>
                    <li><a href="<?= $router->generatePath('budynek-edit', ['id' => $post->getBudynekId()]) ?>">Edit</a></li>
                </ul>
            </li>
        <?php endforeach; ?>
    </ul>

<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
