from .models import Post, Comment

class PostService:
    @staticmethod
    def get_all_posts():
        return Post.objects.all()

    @staticmethod
    def get_post_by_id(post_id):
        return Post.objects.get(pk=post_id)

    @staticmethod
    def create_post(author, title, description, image=None):
        return Post.objects.create(author=author, title=title, description=description, image=image)

    @staticmethod
    def update_post(post, title=None, description=None, image=None):
        if title:
            post.title = title
        if description:
            post.description = description
        if image:
            post.image = image
        post.save()

    @staticmethod
    def delete_post(post):
        post.delete()


class CommentService:
    @staticmethod
    def create_comment(post, author, text):
        return Comment.objects.create(post=post, author=author, text=text)

    @staticmethod
    def delete_comment(comment):
        comment.delete()
