from fastapi import status



STATUS = {
    404 : status.HTTP_404_NOT_FOUND,
    401 : status.HTTP_401_UNAUTHORIZED,
    200 : status.HTTP_200_OK
}