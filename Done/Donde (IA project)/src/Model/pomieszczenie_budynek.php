<?php
namespace App\Model;

use App\Service\Config;

class pomieszczenie_budynek
{
    private ?int $numer = null;
    private ?string $nazwa = null;

    /**
     * @return int|null
     */
    public function getNumer(): ?int
    {
        return $this->numer;
    }

    /**
     * @param int|null $numer
     */
    public function setNumer(?int $numer): void
    {
        $this->numer = $numer;
    }

    /**
     * @return string|null
     */
    public function getNazwa(): ?string
    {
        return $this->nazwa;
    }

    /**
     * @param string|null $nazwa
     */
    public function setNazwa(?string $nazwa): void
    {
        $this->nazwa = $nazwa;
    }


    public static function fromArray($array): pomieszczenie_budynek
    {
        $post = new self();
        $post->fill($array);

        return $post;
    }

    public function fill($array): pomieszczenie_budynek
    {
        if (isset($array['numer'])) {
            $this->setNumer($array['numer']);
        }
        if (isset($array['nazwa'])) {
            $this->setNazwa($array['nazwa']);
        }

        return $this;
    }

    public static function findAll(): array
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM pomieszczenie_budynek';
        $statement = $pdo->prepare($sql);
        $statement->execute();

        $posts = [];
        $postsArray = $statement->fetchAll(\PDO::FETCH_ASSOC);
        foreach ($postsArray as $postArray) {
            $posts[] = self::fromArray($postArray);
        }

        return $posts;
    }

    public static function findnr($numer): ?pomieszczenie_budynek
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM pomieszczenie_budynek WHERE numer = :numer';
        $statement = $pdo->prepare($sql);
        $statement->execute(['numer' => $numer]);

        $postArray = $statement->fetch(\PDO::FETCH_ASSOC);
        if (!$postArray) {
            return null;
        }
        $post = pomieszczenie_budynek::fromArray($postArray);

        return $post;
    }

    public static function findname($name): ?pomieszczenie_budynek
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM pomieszczenie_budynek WHERE nazwa = :name';
        $statement = $pdo->prepare($sql);
        $statement->execute(['name' => $name]);

        $postArray = $statement->fetch(\PDO::FETCH_ASSOC);
        if (!$postArray) {
            return null;
        }
        $post = pomieszczenie_budynek::fromArray($postArray);

        return $post;
    }

    public static function find($name, $numer): ?pomieszczenie_budynek
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM pomieszczenie_budynek WHERE nazwa = :name and numer = :numer';
        $statement = $pdo->prepare($sql);
        $statement->execute(['name' => $name,
            'numer' => $numer
        ]);

        $postArray = $statement->fetch(\PDO::FETCH_ASSOC);
        if (!$postArray) {
            return null;
        }
        $post = pomieszczenie_budynek::fromArray($postArray);

        return $post;
    }
}


