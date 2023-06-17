<?php
    /** @var $Pietro ?\App\Model\Pietro */
?>

<div class="form-group">
    <label for="budynek_id">Budynek_id</label>
    <input type="text" id="budynek_id" name="Pietro[budynek_id]" value="<?= $Pietro ? $Pietro->getBudynekId() : '' ?>">
</div>

<div class="form-group">
    <label for="nazwa">Nazwa</label>
    <textarea id="nazwa" name="Pietro[nazwa]"><?= $Pietro? $Pietro->getNazwa() : '' ?></textarea>
</div>

<div class="form-group">
    <label></label>
    <input type="submit" value="Submit">
</div>
