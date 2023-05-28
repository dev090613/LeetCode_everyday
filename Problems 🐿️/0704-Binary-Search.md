<img src="/Users/isntsoo/Library/Application Support/typora-user-images/image-20230528131531493.png" alt="image-20230528131531493" style="zoom:50%;" />

git filter-branch -f --env-filter "GIT_AUTHOR_NAME=dev090613; GIT_AUTHOR_EMAIL=dev090613@gmail.com; GIT_COMMITTER_NAME='원하는 작성자 이름'; GIT_COMMITTER_EMAIL='원하는 작성자 이메일';" HEAD