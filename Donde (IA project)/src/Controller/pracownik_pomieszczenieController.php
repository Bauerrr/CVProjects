<?php
namespace App\Controller;

use App\Exception\NotFoundException;
use App\Model\pracownik_pomieszczenie;
use App\Model\pracownik;
use App\Service\Router;
use App\Service\Templating;

class pracownik_pomieszczenieController
{
    public function indexAction(Templating $templating, Router $router): ?string
    {
        $pracownicy_pomieszczenia = pracownik_pomieszczenie::findAll();
        $html = $templating->render('pracownik_pomieszczenie/index.html.php', [
            'pracownicy_pomieszczenia' => $pracownicy_pomieszczenia,
            'router' => $router,
        ]);
        return $html;
    }

    public function createAction(?array $requestPracownik_Pomieszczenie, Templating $templating, Router $router): ?string
    {
        if ($requestPracownik_Pomieszczenie) {
            $pracownik_pomieszczenie = pracownik_pomieszczenie::fromArray($requestPracownik_Pomieszczenie);
            // @todo missing validation
            $pracownik_pomieszczenie->save();

            $path = $router->generatePath('pracownik_pomieszczenie-index');
            $router->redirect($path);
            return null;
        } else {
            $pracownik_pomieszczenie = new pracownik_pomieszczenie();
        }

        $html = $templating->render('pracownik_pomieszczenie/create.html.php', [
            'pracownik_pomieszczenie' => $pracownik_pomieszczenie,
            'router' => $router,
        ]);
        return $html;
    }

    public function createActionAll(?array $requestPracownik, ?array $requestPietro, ?array $requestPomieszczenie, Templating $templating, Router $router): ?string
    {
        if ($requestPracownik && $requestPomieszczenie && $requestPietro) {
            $pracownik = pracownik::findname($requestPracownik['imie'], $requestPracownik['nazwisko']);
            // @todo missing validation
            $pietro = Pietro::findName($requestPietro['nazwa']);
            $pomieszczenie = pomieszczenie::findPomPietro($requestPomieszczenie['numer'], $pietro->getPietroId());

            $pracownik_pomieszczenie = [
                'pomieszczenie_id' =>$pomieszczenie->getPomieszczenie_id(),
                'pracownik_id' =>$pracownik->getPracownikId(), 
            ];
            $pracownik_pomieszczenie2 = pracownik_pomieszczenie::fromArray($pracownik_pomieszczenie);
            $pracownik_pomieszczenie2->save();

            $path = $router->generatePath('pracownik_pomieszczenie-index');
            $router->redirect($path);
            return null;
        } else {
            $pracownik_pomieszczenie = new pracownik_pomieszczenie();
        }

        $html = $templating->render('pracownik_pomieszczenie/create.html.php', [
            'pracownik_pomieszczenie' => $pracownik_pomieszczenie,
            'router' => $router,
        ]);
        return $html;
    }

    public function editAction(int $pracownik_pomieszczenieId, ?array $requestPracownik_Pomieszczenie, Templating $templating, Router $router): ?string
    {
        $pracownik_pomieszczenie = pracownik_pomieszczenie::find($pracownik_pomieszczenieId);
        if (! $pracownik_pomieszczenie) {
            throw new NotFoundException("Missing pomieszczenie with id $pracownik_pomieszczenieId");
        }

        if ($requestPracownik_Pomieszczenie) {
            $pracownik_pomieszczenie->fill($requestPracownik_Pomieszczenie);
            // @todo missing validation
            $pracownik_pomieszczenie->save();

            $path = $router->generatePath('pracownik_pomieszczenie-index');
            $router->redirect($path);
            return null;
        }

        $html = $templating->render('pracownik_pomieszczenie/edit.html.php', [
            'pracownik_pomieszczenie' => $pracownik_pomieszczenie,
            'router' => $router,
        ]);
        return $html;
    }

    public function showAction(int $pracownik_pomieszczenieId, Templating $templating, Router $router): ?string
    {
        $pracownik_pomieszczenie = pracownik_pomieszczenie::find($pracownik_pomieszczenieId);
        if (! $pracownik_pomieszczenie) {
            throw new NotFoundException("Missing pomieszczenie with id $pracownik_pomieszczenieId");
        }

        $html = $templating->render('pracownik_pomieszczenie/show.html.php', [
            'pracownik_pomieszczenie' => $pracownik_pomieszczenie,
            'router' => $router,
        ]);
        return $html;
    }

    public function deleteAction(int $pracownik_pomieszczenieId, Router $router): ?string
    {
        $pracownik_pomieszczenie = pracownik_pomieszczenie::find($pracownik_pomieszczenieId);
        if (! $pracownik_pomieszczenie) {
            throw new NotFoundException("Missing pomieszczenie with id $pracownik_pomieszczenieId");
        }

        $pracownik_pomieszczenie->delete();
        $path = $router->generatePath('pracownik_pomieszczenie-index');
        $router->redirect($path);
        return null;
    }
}
