<?php

/** @var \App\Model\Pietro $Pietro */
/** @var \App\Service\Router $router */

$title = 'Create Pietro';
$bodyClass = "edit";

ob_start();
session_start();?>
    <h1>Create Pietro</h1>
    <form action="<?= $router->generatePath('Pietro-create') ?>" method="post" class="edit-form">
        <?php require __DIR__ . DIRECTORY_SEPARATOR . '_form.html.php'; ?>
        <input type="hidden" name="action" value="Pietro-create">
    </form>

    <a href="<?= $router->generatePath('Pietro-index') ?>">Back to list</a>
<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
