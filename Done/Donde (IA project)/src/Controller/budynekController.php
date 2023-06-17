<?php
namespace App\Controller;

use App\Exception\NotFoundException;
use App\Model\budynek;
use App\Service\Router;
use App\Service\Templating;

class budynekController
{
    public function indexAction(Templating $templating, Router $router): ?string
    {
        $posts = budynek::findAll();
        $html = $templating->render('budynek/index.html.php', [
            'posts' => $posts,
            'router' => $router,
        ]);
        return $html;
    }

    public function createAction(?array $requestPost, Templating $templating, Router $router): ?string
    {
        if ($requestPost) {
            $post = budynek::fromArray($requestPost);
            // @todo missing validation
            $post->save();

            $path = $router->generatePath('budynek-index');
            $router->redirect($path);
            return null;
        } else {
            $post = new budynek();
        }

        $html = $templating->render('budynek/create.html.php', [
            'post' => $post,
            'router' => $router,
        ]);
        return $html;
    }

    public function editAction(int $postId, ?array $requestPost, Templating $templating, Router $router): ?string
    {
        $post = budynek::find($postId);
        if (! $post) {
            throw new NotFoundException("Missing budynek with id $postId");
        }

        if ($requestPost) {
            $post->fill($requestPost);
            // @todo missing validation
            $post->save();

            $path = $router->generatePath('budynek-index');
            $router->redirect($path);
            return null;
        }

        $html = $templating->render('budynek/edit.html.php', [
            'post' => $post,
            'router' => $router,
        ]);
        return $html;
    }

    public function showAction(int $postId, Templating $templating, Router $router): ?string
    {
        $post = budynek::find($postId);
        if (! $post) {
            throw new NotFoundException("Missing budynek with id $postId");
        }

        $html = $templating->render('budynek/show.html.php', [
            'post' => $post,
            'router' => $router,
        ]);
        return $html;
    }

    public function deleteAction(int $postId, Router $router): ?string
    {
        $post = budynek::find($postId);
        if (! $post) {
            throw new NotFoundException("Missing budynek with id $postId");
        }

        $post->delete();
        $path = $router->generatePath('budynek-index');
        $router->redirect($path);
        return null;
    }
}
