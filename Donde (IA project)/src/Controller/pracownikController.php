<?php
namespace App\Controller;

use App\Exception\NotFoundException;
use App\Model\pracownik;
use App\Service\Router;
use App\Service\Templating;

class pracownikController
{
    public function indexAction(Templating $templating, Router $router): ?string
    {
        $posts = pracownik::findAll();
        $html = $templating->render('pracownik/index.html.php', [
            'posts' => $posts,
            'router' => $router,
        ]);
        return $html;
    }

    public function createAction(?array $requestPost, Templating $templating, Router $router): ?string
    {
        if ($requestPost) {
            $post = pracownik::fromArray($requestPost);
            // @todo missing validation
            $post->save();

            $path = $router->generatePath('pracownik-index');
            $router->redirect($path);
            return null;
        } else {
            $post = new pracownik();
        }

        $html = $templating->render('pracownik/create.html.php', [
            'post' => $post,
            'router' => $router,
        ]);
        return $html;
    }

    public function editAction(int $postId, ?array $requestPost, Templating $templating, Router $router): ?string
    {
        $post = pracownik::find($postId);
        if (! $post) {
            throw new NotFoundException("Missing post with id $postId");
        }

        if ($requestPost) {
            $post->fill($requestPost);
            // @todo missing validation
            $post->save();

            $path = $router->generatePath('pracownik-index');
            $router->redirect($path);
            return null;
        }

        $html = $templating->render('pracownik/edit.html.php', [
            'post' => $post,
            'router' => $router,
        ]);
        return $html;
    }

    public function showAction(int $postId, Templating $templating, Router $router): ?string
    {
        $post = pracownik::find($postId);
        if (! $post) {
            throw new NotFoundException("Missing post with id $postId");
        }

        $html = $templating->render('pracownik/show.html.php', [
            'post' => $post,
            'router' => $router,
        ]);
        return $html;
    }

    public function deleteAction(int $postId, Router $router): ?string
    {
        $post = pracownik::find($postId);
        if (! $post) {
            throw new NotFoundException("Missing post with id $postId");
        }

        $post->delete();
        $path = $router->generatePath('pracownik-index');
        $router->redirect($path);
        return null;
    }
}
