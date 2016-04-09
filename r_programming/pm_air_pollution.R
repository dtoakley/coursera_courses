get_tables <- function(directory) {
  all_files <- dir(directory, pattern = '\\.csv', full.names = TRUE)
  return(data_tables <- lapply(all_files, read.csv))
}

pollutantmean <- function(directory, pollutant, id = 1:332) {
  data_tables <- get_tables(directory)
  pollutant_data <- c()
  
  for (table in data_tables[id]) {
    pollutant_data <- c(pollutant_data, table[[pollutant]])
  }
  pollutant_mean <- mean(pollutant_data, na.rm=TRUE)
}

complete <- function(directory, id = 1: 332) {
  data_tables <- get_tables(directory)
  nobs_matrix <- matrix(NA, 0, 2)
  colnames(nobs_matrix) <-list("id", "nobs")
  
  for (table in data_tables[id]) {
    complete_total <- sum(!is.na(table[,2]))
    table_id <- table[[4]][[1]]
    nobs_matrix <- rbind(nobs_matrix, c(table_id, complete_total))
  }
  return(as.data.frame(nobs_matrix))
}

corr <- function(directory, threshold = 0) {
  data_tables <- get_tables(directory)
  result <- c()
  
  for (table in data_tables) {
    if (meets_threshold(table, threshold)) {
      correlations <- cor(table$sulfate , table$nitrate, use = "pairwise.complete.obs")
      result <- c(result, correlations)
    }
  }
  return(result)
}

meets_threshold <- function(table, threshold) {
  if (sum(!is.na(table[,2])) >= threshold) {
    return(TRUE)
  } 
  else {
    return(FALSE)
  }
}





