
best <- function(state, outcome) {
  outcome_map = list("heart attack" = 11, "heart failure" = 17, "pneumonia" = 23)
  
  ## Read outcome data
  data <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  col_num <- (outcome_map[[outcome]])
  
  state_subset <- subset(data,State == state)[, col_num]
  print(state_subset)

  
  ## Check that state and outcome are valid
  if (!(state %in% data[, 7])) {
    stop("invalid state")
  }
  if (!(outcome %in% names(outcome_map))) {
    stop("invalid outcome")
  }
  
  ## Return hospital name in that state with lowest 30-day death
  
  ## rate
}

best("TX", "heart attack")
#print(best("TX", "heart failure"))