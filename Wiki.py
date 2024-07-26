import wikipedia

# Ask for the word to scrape for as well as depth of search
query = input()
depth = input()

# Initialize a list to store search results
list = wikipedia.search(query)

# Convert depth to an integer
depth = int(depth)
i = 0

# Iterate over the existing results and branch off based on depth
while i < depth and i < len(list):
    try:
        list.extend(wikipedia.search(list[i]))
        i += 1
    except Exception as e:
        # Handle any exception (including base exceptions)
        print(f"Error processing {list[i]}: {e}")



# scrape data from wiki
file_name = "text2.txt"
with open(file_name, "a") as file:
    search_results = list
    for result in search_results:
        try:
            summary = wikipedia.page(result).content
            file.write(f"{result}:\n{summary}\n\n")
        except wikipedia.exceptions.DisambiguationError:
            # Skip disambiguation pages
            print(f"Skipping disambiguation page: {result}")
        except wikipedia.exceptions.PageError:
            # Skip pages that don't exist
            print(f"Skipping non-existent page: {result}")
        except Exception as e:
            # Handle any exception (including base exceptions)
            print(f"Error processing {result}: {e}")




