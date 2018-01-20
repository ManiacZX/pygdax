param (
  [Parameter(Mandatory=$True,Position=1)]
  [string]$days
)

docker run -v ${PWD}/src:/src -v ${PWD}/out:/out my/pygdax $days