from fastapi import Response, status, HTTPException, Depends, APIRouter
from pydantic.types import conint
from sqlalchemy.orm import Session
from app import models, schemas, oauth2
from app.database import get_db



router = APIRouter(
    prefix="/vote",
    tags=['Vote']
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, response: Response, db: Session = Depends(get_db),
            current_user: models.User = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {vote.post_id} not found")

    found_vote = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, 
        models.Vote.user_id == current_user.id).first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                detail=f"User {current_user.email} already voted on post {found_vote.post_id}")
        new_vote = models.Vote(user_id=current_user.id, post_id=vote.post_id)
        db.add(new_vote)
        db.commit()
        return Response(status_code=status.HTTP_201_CREATED, content=f"Succesfully voted on post {new_vote.post_id}")
    else:
        if not found_vote:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exists")
        else:
            db.delete(found_vote)
            db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT, content="Succesfully deleted vote")
        
            
