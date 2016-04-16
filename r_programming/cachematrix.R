## This function takes a matrix object and returns a list of methods available:
## set matrix, get matrix, set metrix inverse, get matrix inverse

makeCacheMatrix <- function(x = matrix()) {
  inverse <<- NULL
  set <- function(y) {
    x <<- y
    inverse <<- NULL 
  }
  get <- function() x
  setInverse <- function(i) inverse <<- i
  getInverse <- function() inverse
  list(set = set, get = get, 
       setInverse = setInverse,
       getInverse = getInverse)
}


## This function takes the list of functions returned by makeCacheMatrix. 
## If the matrix inverse is cached it returns it. Otherwise it creates, 
## caches it and the returns the matrix inverse. 

cacheSolve <- function(x, ...) {
  inverse <- x$getInverse()
  if (!is.null(inverse)) {
    return(inverse)
  }
  m <- x$get()
  inverse <- solve(m)
  x$setInverse(inverse)
  inverse
}
