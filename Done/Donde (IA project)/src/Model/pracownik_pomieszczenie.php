<?php
namespace App\Model;

use App\Service\Config;

class pracownik_pomieszczenie
{
    private ?int $pracownik_pomieszczenie_id = null;
    private ?int $pracownik_id = null;
    private ?int $pomieszczenie_id = null;

    /**
     * Get the value of pracownik_pomieszczenie_id
     */ 
    public function getPracownik_pomieszczenie_id() : ?int
    {
        return $this->pracownik_pomieszczenie_id;
    }

    /**
     * Set the value of pracownik_pomieszczenie_id
     *
     * @return  self
     */ 
    public function setPracownik_pomieszczenie_id($pracownik_pomieszczenie_id) : void
    {
        $this->pracownik_pomieszczenie_id = $pracownik_pomieszczenie_id;
        
    }

    /**
     * Get the value of pracownik_id
     */ 
    public function getPracownik_id() : ?int
    {
        return $this->pracownik_id;
    }

    /**
     * Set the value of pracownik_id
     *
     * @return  self
     */ 
    public function setPracownik_id($pracownik_id) : void
    {
        $this->pracownik_id = $pracownik_id;

    }

    /**
     * Get the value of pomieszczenie_id
     */ 
    public function getPomieszczenie_id() : ?int
    {
        return $this->pomieszczenie_id;
    }

    /**
     * Set the value of pomieszczenie_id
     *
     * @return  self
     */ 
    public function setPomieszczenie_id($pomieszczenie_id) : void
    {
        $this->pomieszczenie_id = $pomieszczenie_id;

    }

    public static function fromArray($array): pracownik_pomieszczenie
    {
        $pracownik_pomieszczenie = new self();
        $pracownik_pomieszczenie->fill($array);

        return $pracownik_pomieszczenie;
    }

    public function fill($array): pracownik_pomieszczenie
    {
        if (isset($array['pracownik_pomieszczenie_id']) && ! $this->getPracownik_pomieszczenie_id()) {
            $this->setPracownik_pomieszczenie_id($array['pracownik_pomieszczenie_id']);
        }
        if (isset($array['pracownik_id'])) {
            $this->setPracownik_id($array['pracownik_id']);
        }
        if (isset($array['pomieszczenie_id'])) {
            $this->setPomieszczenie_id($array['pomieszczenie_id']);
        }

        return $this;
    }


    public static function findAll(): array
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM pracownik_pomieszczenie';
        $statement = $pdo->prepare($sql);
        $statement->execute();

        $pracownicy_pomieszczenia = [];
        $pracownicy_pomieszczeniaArray = $statement->fetchAll(\PDO::FETCH_ASSOC);
        foreach ($pracownicy_pomieszczeniaArray as $pracownik_pomieszczenieArray) {
            $pracownicy_pomieszczenia[] = self::fromArray($pracownik_pomieszczenieArray);
        }

        return $pracownicy_pomieszczenia;
    }

    public static function find($pracownik_pomieszczenie_id): ?pracownik_pomieszczenie
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM pracownik_pomieszczenie WHERE pracownik_pomieszczenie_id = :pracownik_pomieszczenie_id';
        $statement = $pdo->prepare($sql);
        $statement->execute(['pracownik_pomieszczenie_id' => $pracownik_pomieszczenie_id]);

        $pracownik_pomieszczenieArray = $statement->fetch(\PDO::FETCH_ASSOC);
        if (! $pracownik_pomieszczenieArray) {
            return null;
        }
        $pracownik_pomieszczenie = pracownik_pomieszczenie::fromArray($pracownik_pomieszczenieArray);

        return $pracownik_pomieszczenie;
    }

    public static function findprac($pracownikid): ?array
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM pracownik_pomieszczenie WHERE pracownik_id = :pracownik_id';
        $statement = $pdo->prepare($sql);
        $statement->execute(['pracownik_id' => $pracownikid]);

        $pracownicy_pomieszczenia = [];
        $pracownicy_pomieszczeniaArray = $statement->fetchAll(\PDO::FETCH_ASSOC);
        foreach ($pracownicy_pomieszczeniaArray as $pracownik_pomieszczenieArray) {
            $pracownicy_pomieszczenia[] = self::fromArray($pracownik_pomieszczenieArray);
        }

        return $pracownicy_pomieszczenia;
    }

    public function save(): void
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        if (! $this->getPracownik_pomieszczenie_id()) {
            $sql = "INSERT INTO pracownik_pomieszczenie (pracownik_id, pomieszczenie_id) VALUES (:pracownik_id, :pomieszczenie_id)";
            $statement = $pdo->prepare($sql);
            $statement->execute([
                'pracownik_id' => $this->getPracownik_id(),
                'pomieszczenie_id' => $this->getPomieszczenie_id(),
            ]);

            $this->setPracownik_pomieszczenie_id($pdo->lastInsertId());
        } else {
            $sql = "UPDATE pracownik_pomieszczenie SET pracownik_id = :pracownik_id, pomieszczenie_id = :pomieszczenie_id WHERE pracownik_pomieszczenie_id = :pracownik_pomieszczenie_id";
            $statement = $pdo->prepare($sql);
            $statement->execute([
                ':pracownik_id' => $this->getPracownik_id(),
                ':pomieszczenie_id' => $this->getPomieszczenie_id(),
                ':pracownik_pomieszczenie_id' => $this->getPracownik_pomieszczenie_id(),
            ]);
        }
    }

    
    public function delete(): void
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = "DELETE FROM pracownik_pomieszczenie WHERE pracownik_pomieszczenie_id = :pracownik_pomieszczenie_id";
        $statement = $pdo->prepare($sql);
        $statement->execute([
            ':pracownik_pomieszczenie_id' => $this->getPracownik_pomieszczenie_id(),
        ]);

        $this->setPracownik_pomieszczenie_id(null);
        $this->setPracownik_id(null);
        $this->setPomieszczenie_id(null);
    }


}
