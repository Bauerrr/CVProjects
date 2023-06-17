<?php

/** @var \App\Model\budynek $post */
/** @var \App\Service\Router $router */

$title = 'Create budynek';
$bodyClass = "edit";

ob_start(); ?>
    <h1>Create budynek</h1>
    <form action="<?= $router->generatePath('budynek-create') ?>" method="post" class="edit-form">
        <?php require __DIR__ . DIRECTORY_SEPARATOR . '_form.html.php'; ?>
        <input type="hidden" name="action" value="budynek-create">
    </form>

    <a href="<?= $router->generatePath('budynek-index') ?>">Back to list</a>
<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
