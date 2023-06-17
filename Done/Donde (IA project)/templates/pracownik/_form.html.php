<?php
    /** @var $post ?\App\Model\pracownik */
?>

<div class="form-group">
    <label for="imie">Imie</label>
    <input type="text" id="imie" name="pracownik[imie]" value="<?= $post ? $post->getImie() : '' ?>">
</div>

<div class="form-group">
    <label for="nazwisko">Nazwisko</label>
    <input type="text" id="nazwisko" name="pracownik[nazwisko]" value="<?= $post? $post->getNazwisko() : '' ?>">
</div>
<div class="form-group">
    <label for="tytul">Tytul</label>
    <input type="text" id="tytul" name="pracownik[tytul]" value="<?= $post? $post->getTytul() : '' ?>">
</div>
<div class="form-group">
    <label for="gabinet">Gabinet</label>
    <input type="text" id="gabinet" name="pracownik[gabinet]" value="<?= $post? $post->getGabinet() : '' ?>">
</div>
<div class="form-group">
    <label></label>
    <input type="submit" value="Submit">
</div>
