<?php
    
    /** @var $pracownik_pomieszczenie ?\App\Model\pracownik_pomieszczenie */
    use App\Model\pracownik;
    use App\Model\pomieszczenie;
    use App\Model\Pietro;
    // imie i nazwisko pracownika, nazwe pietra, nr pomieszczenia
    //pracownik::find($pracownik_pomieszczenie->getPracownik_id())->getImie()
    error_reporting(E_ALL);
?>

<div class="form-group">
    <label for="imie">Imie</label> 
    <input type="text" id="imie" name="pracownik[imie]" value="<?= $pracownik_pomieszczenie ? $pracownik_pomieszczenie->getPracownik_id() : '' ?>">
</div>

<div class="form-group">
    <label for="nazwisko">Nazwisko</label>
    <input type="text" id="nazwisko" name="pracownik[nazwisko]" value="<?= $pracownik_pomieszczenie ? pracownik::find($pracownik_pomieszczenie->getPracownik_id())->getNazwisko() : '' ?>">
</div>
<div class="form-group">
    <label for="tytul">Nazwa Pietra</label>
    <input type="text" id="tytul" name="Pietro[nazwa]" value="<?= $pracownik_pomieszczenie ? Pietro::find(pomieszczenie::find($pracownik_pomieszczenie->getPomieszczenie_id())->getPietro_id())->getNazwa() : '' ?>">
</div>
<div class="form-group">
    <label for="gabinet">Nr Pomieszczenia</label>
    <input type="text" id="gabinet" name="pomieszczenie[numer]" value="<?= $pracownik_pomieszczenie ? pomieszczenie::find($pracownik_pomieszczenie->getPomieszczenie_id())->getNumer() : '' ?>">
</div>
<div class="form-group">
    <label></label>
    <input type="submit" value="Submit">
</div>
