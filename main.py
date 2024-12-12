-- Tạo GUI cho nút Start và Stop
local Player = game.Players.LocalPlayer
local ScreenGui = Instance.new("ScreenGui")
ScreenGui.Parent = Player.PlayerGui

local StartButton = Instance.new("TextButton")
StartButton.Parent = ScreenGui
StartButton.Size = UDim2.new(0, 200, 0, 50)
StartButton.Position = UDim2.new(0.5, -100, 0.5, -25)
StartButton.Text = "Start Flying"
StartButton.BackgroundColor3 = Color3.fromRGB(0, 255, 0)

local StopButton = Instance.new("TextButton")
StopButton.Parent = ScreenGui
StopButton.Size = UDim2.new(0, 200, 0, 50)
StopButton.Position = UDim2.new(0.5, -100, 0.5, 25)
StopButton.Text = "Stop Flying"
StopButton.BackgroundColor3 = Color3.fromRGB(255, 0, 0)

local flying = false -- Trạng thái bay
local speed = 50 -- Tốc độ bay
local bodyGyro, bodyVelocity

-- Hàm bắt đầu bay
local function startFlying()
    local Character = Player.Character or Player.CharacterAdded:Wait()
    local HumanoidRootPart = Character:WaitForChild("HumanoidRootPart")

    -- Tạo BodyGyro và BodyVelocity
    bodyGyro = Instance.new("BodyGyro", HumanoidRootPart)
    bodyVelocity = Instance.new("BodyVelocity", HumanoidRootPart)

    bodyGyro.P = 9e4
    bodyGyro.MaxTorque = Vector3.new(9e4, 9e4, 9e4)
    bodyGyro.CFrame = HumanoidRootPart.CFrame

    bodyVelocity.MaxForce = Vector3.new(9e4, 9e4, 9e4)
    bodyVelocity.Velocity = Vector3.zero

    -- Đặt trạng thái bay là true
    flying = true

    -- Xử lý di chuyển khi bay
    game:GetService("RunService").RenderStepped:Connect(function()
        if flying then
            local moveDirection = Vector3.zero
            if UserInputService:IsKeyDown(Enum.KeyCode.W) then
                moveDirection = moveDirection + workspace.CurrentCamera.CFrame.LookVector
            end
            if UserInputService:IsKeyDown(Enum.KeyCode.S) then
                moveDirection = moveDirection - workspace.CurrentCamera.CFrame.LookVector
            end
            if UserInputService:IsKeyDown(Enum.KeyCode.A) then
                moveDirection = moveDirection - workspace.CurrentCamera.CFrame.RightVector
            end
            if UserInputService:IsKeyDown(Enum.KeyCode.D) then
                moveDirection = moveDirection + workspace.CurrentCamera.CFrame.RightVector
            end
            bodyVelocity.Velocity = moveDirection * speed
            bodyGyro.CFrame = workspace.CurrentCamera.CFrame
        else
            bodyVelocity.Velocity = Vector3.zero
        end
    end)
end

-- Hàm dừng bay
local function stopFlying()
    flying = false
    if bodyGyro then
        bodyGyro:Destroy()
    end
    if bodyVelocity then
        bodyVelocity:Destroy()
    end
end

-- Gắn sự kiện cho nút Start
StartButton.MouseButton1Click:Connect(function()
    startFlying()
    StartButton.Visible = false
    StopButton.Visible = true
end)

-- Gắn sự kiện cho nút Stop
StopButton.MouseButton1Click:Connect(function()
    stopFlying()
    StartButton.Visible = true
    StopButton.Visible = false
end)

-- Ẩn nút Stop khi bắt đầu
StopButton.Visible = false
