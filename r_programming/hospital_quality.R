data <- read.csv("outcome-of-care-measures.csv", colClasses = "character", na.strings = "Not Available" )
possible_outcomes <- list("heart attack"=11,"heart failure"=17, "pneumonia"=23)

best <- function(state, outcome) {
  
  ## Check that state and outcome are valid
  if (!(state %in% data[,7])) stop("invalid state")
  if (!(outcome %in% names(possible_outcomes))) stop("invalid outcome")
  
  ## Return hospital name in that state with lowest 30-day death
  outcome_col <- possible_outcomes[outcome][[1]]
  state_data <- data[data$State==state,]
  x <- which.min(state_data[,outcome_col])
  state_data[x, 2]
  
}

# print(best("TX", "heart attack"))
# print(best("TX", "heart failure"))
# print(best("BB", "heart attack"))
# print(best("NY", "hert attack"))

rankhospital <- function(state, outcome, num = "best") {

  ## Check that state and outcome are valid
  if (!(state %in% data[,7])) stop("invalid state")
  if (!(outcome %in% names(possible_outcomes))) stop("invalid outcome")
  
  ## Return hospital name in that state with the given rank
  state_data <- data[data$State==state,]
  outcome_col <- possible_outcomes[outcome][[1]]
  sorted_state_data <- state_data[order(as.numeric(state_data[[outcome_col]]), state_data[[2]]),]
  
  if (num == "best") num <- 1
  if (num == "worst") num <- nrow(sorted_state_data)
  
  sorted_state_data[num, 2]
  
}
# print(rankhospital("TX", "heart failure", 4))
# print(rankhospital("MD", "heart attack", "worst"))
# print(rankhospital("MN", "heart attack", 5000))

rankall <- function(outcome, num = "best") {

  ## For each state, find the hospital of the given rank
  state <- unique(data[, 7])
  hospital <- vector(mode="character")           
  
  for (i in seq(state)) {
    hospital[i] <- rankhospital(state[i], outcome, num)
  }
  
  ## Return a data frame with the hospital names and the
  data.frame(hospital, state)
}


