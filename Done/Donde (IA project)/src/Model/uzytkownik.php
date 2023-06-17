<?php
namespace App\Model;

use App\Service\Config;

class uzytkownik
{
    private ?int $uzytkownik_id = null;
    private ?string $log = null;
    private ?string $haslo = null;

    /**
     * @return int|null
     */
    public function getUzytkownikId(): ?int
    {
        return $this->uzytkownik_id;
    }

    /**
     * @param int|null $uzytkownik_id
     */
    public function setUzytkownikId(?int $uzytkownik_id): void
    {
        $this->uzytkownik_id = $uzytkownik_id;
    }

    /**
     * @return string|null
     */
    public function getLog(): ?string
    {
        return $this->log;
    }

    /**
     * @param string|null $log
     */
    public function setLog(?string $log): void
    {
        $this->log = $log;
    }

    /**
     * @return string|null
     */
    public function getHaslo(): ?string
    {
        return $this->haslo;
    }

    /**
     * @param string|null $haslo
     */
    public function setHaslo(?string $haslo): void
    {
        $this->haslo = $haslo;
    }


    public static function fromArray($array): uzytkownik
    {
        $uzytkownik = new self();
        $uzytkownik->fill($array);

        return $uzytkownik;
    }

    public function fill($array): uzytkownik
    {
        if (isset($array['uzytkownik_id']) && ! $this->getUzytkownikId()) {
            $this->setUzytkownikId($array['uzytkownik_id']);
        }
        if (isset($array['log'])) {
            $this->setLog($array['log']);
        }
        if (isset($array['haslo'])) {
            $this->setHaslo($array['haslo']);
        }

        return $this;
    }

    public static function find($login): ?uzytkownik
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM uzytkownik WHERE log = :log';
        $statement = $pdo->prepare($sql);
        $statement->execute(['log' => $login]);

        $uzytkownikArray = $statement->fetch(\PDO::FETCH_ASSOC);
        if (! $uzytkownikArray) {
            return null;
        }
        $uzytkownik = uzytkownik::fromArray($uzytkownikArray);

        return $uzytkownik;
    }
    public static function find_id($login_id): ?uzytkownik
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM uzytkownik WHERE uzytkownik_id = :uzytkownik_id';
        $statement = $pdo->prepare($sql);
        $statement->execute(['uzytkownik_id' => $login_id]);

        $uzytkownikArray = $statement->fetch(\PDO::FETCH_ASSOC);
        if (! $uzytkownikArray) {
            return null;
        }
        $uzytkownik = uzytkownik::fromArray($uzytkownikArray);

        return $uzytkownik;
    }
}
